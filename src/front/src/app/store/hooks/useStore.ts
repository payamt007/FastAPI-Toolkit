import {useEffect, useState} from 'react';
import {useStore as useZustandStore} from '@/app/store';

// For use in components (handles hydration issues)
export function useAuth<T>(selector: (state: import('@/app/store').StoreState) => T) {
    const [hydrated, setHydrated] = useState(false);
    useEffect(() => setHydrated(true), []);

    const state = useZustandStore(selector);

    // Return empty data during SSR
    if (!hydrated) {
        return selector({
            user: null,
            token: null,
            isAuthenticated: false,
            isLoading: false,
            error: null,
            login: async () => {
            },
            logout: () => {
            },
            clearError: () => {
            },
        } as any);
    }

    return state;
}