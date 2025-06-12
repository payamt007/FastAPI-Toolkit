'use client'

import {useTheme} from '@/app/context/ThemeContext'
import {Sun, Moon, Monitor} from 'lucide-react'

export default function ThemeToggle() {
    const {theme, setTheme} = useTheme()

    const themes = [
        {value: 'light' as const, icon: Sun, label: 'Light'},
        {value: 'dark' as const, icon: Moon, label: 'Dark'},
        {value: 'system' as const, icon: Monitor, label: 'System'},
    ]

    return (
        <div className="flex items-center space-x-2 p-2 bg-gray-100 dark:bg-gray-800 rounded-lg">
            {themes.map(({value, icon: Icon, label}) => (
                <button
                    key={value}
                    onClick={() => setTheme(value)}
                    className={`
            flex items-center space-x-2 px-3 py-2 rounded-md transition-colors
            ${theme === value
                        ? 'bg-blue-500 text-white'
                        : 'text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700'
                    }
          `}
                    title={`Switch to ${label} theme`}
                >
                    <Icon size={16}/>
                    <span className="text-sm">{label}</span>
                </button>
            ))}
        </div>
    )
}