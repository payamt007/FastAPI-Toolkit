'use client'

import { useTheme } from '@/app/context/ThemeContext'
import React from "react";

interface ThemedCardProps {
  title: string
  children: React.ReactNode
}

export default function ThemedCard({ title, children }: ThemedCardProps) {
  const { theme, actualTheme } = useTheme()

  return (
    <div className="max-w-md mx-auto bg-white dark:bg-gray-800 shadow-lg rounded-lg overflow-hidden transition-colors duration-200">
      <div className="px-6 py-4">
        <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-2">
          {title}
        </h3>
        <div className="text-gray-700 dark:text-gray-300 mb-4">
          {children}
        </div>
        <div className="text-sm text-gray-500 dark:text-gray-400">
          <p>Current theme setting: <span className="font-medium">{theme}</span></p>
          <p>Actual theme: <span className="font-medium">{actualTheme}</span></p>
        </div>
      </div>
    </div>
  )
}