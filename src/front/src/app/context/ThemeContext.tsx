'use client'

import {createContext, useContext, useState, useEffect, ReactNode} from 'react'

// Define theme types
export type Theme = 'light' | 'dark' | 'system'

interface ThemeContextType {
    theme: Theme
    actualTheme: 'light' | 'dark' // The resolved theme (system becomes light/dark)
    setTheme: (theme: Theme) => void
}

// Create the context with default values
const ThemeContext = createContext<ThemeContextType | undefined>(undefined)

// Custom hook to use the theme context
export function useTheme() {
    const context = useContext(ThemeContext)
    if (context === undefined) {
        throw new Error('useTheme must be used within a ThemeProvider')
    }
    return context
}

// Theme provider component
interface ThemeProviderProps {
    children: ReactNode
    defaultTheme?: Theme
}

export function ThemeProvider({
                                  children,
                                  defaultTheme = 'system'
                              }: ThemeProviderProps) {
    const [theme, setTheme] = useState<Theme>(defaultTheme)
    const [actualTheme, setActualTheme] = useState<'light' | 'dark'>('light')

    // Function to get system theme preference
    const getSystemTheme = (): 'light' | 'dark' => {
        if (typeof window !== 'undefined') {
            return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
        }
        return 'light'
    }

    // Update actual theme based on theme setting
    useEffect(() => {
        const updateActualTheme = () => {
            if (theme === 'system') {
                setActualTheme(getSystemTheme())
            } else {
                setActualTheme(theme)
            }
        }

        updateActualTheme()

        // Listen for system theme changes when theme is set to 'system'
        if (theme === 'system') {
            const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)')
            const handleChange = () => updateActualTheme()

            mediaQuery.addEventListener('change', handleChange)
            return () => mediaQuery.removeEventListener('change', handleChange)
        }
    }, [theme])

    // Apply theme to document
    useEffect(() => {
        const root = document.documentElement
        root.classList.remove('light', 'dark')
        root.classList.add(actualTheme)
    }, [actualTheme])

    // Load theme from localStorage on mount
    useEffect(() => {
        const savedTheme = localStorage.getItem('theme') as Theme
        if (savedTheme && ['light', 'dark', 'system'].includes(savedTheme)) {
            setTheme(savedTheme)
        }
    }, [])

    // Save theme to localStorage when it changes
    const handleThemeChange = (newTheme: Theme) => {
        setTheme(newTheme)
        localStorage.setItem('theme', newTheme)
    }

    const value: ThemeContextType = {
        theme,
        actualTheme,
        setTheme: handleThemeChange,
    }

    return (
        <ThemeContext.Provider value={value}>
            {children}
        </ThemeContext.Provider>
    )
}