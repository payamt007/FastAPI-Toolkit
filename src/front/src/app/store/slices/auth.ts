// /src/store/slices/auth.ts
import { StateCreator } from 'zustand';

export interface AuthState {
  user: { username: string } | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;

  // Actions
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
  clearError: () => void;
}

export const createAuthSlice: StateCreator<AuthState> = (set) => ({
  user: null,
  token: null,
  isAuthenticated: false,
  isLoading: false,
  error: null,

  login: async (username, password) => {
    set({ isLoading: true, error: null });
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      if (!response.ok) throw new Error('Login failed');

      const data = await response.json();
      set({
        user: { username: data.username },
        token: data.token,
        isAuthenticated: true,
        isLoading: false
      });
    } catch (error) {
      set({ error: 'Login failed. Please check your credentials.', isLoading: false });
    }
  },

  logout: () => {
    set({ user: null, token: null, isAuthenticated: false });
  },

  clearError: () => {
    set({ error: null });
  }
});