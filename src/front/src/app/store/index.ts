// /src/store/index.ts
import {create} from 'zustand';
import {createAuthSlice, AuthState} from './slices/auth';
import {persist, createJSONStorage} from 'zustand/middleware';

// Define the store type
export type StoreState = AuthState;

// Create store with persistence
export const useStore = create<StoreState>()(
    persist(
        (...a) => ({
            ...createAuthSlice(...a),
        }),
        {
            name: 'app-storage',
            storage: createJSONStorage(() => localStorage),
        }
    )
);