// Need to use the React-specific entry point to import `createApi`
import {createApi, fetchBaseQuery} from "@reduxjs/toolkit/query/react";

interface getTokenResponse {
    "access_token": string,
    "token_type": string
}

// Define a service using a base URL and expected endpoints
export const authApiSlice = createApi({
    baseQuery: fetchBaseQuery({baseUrl: "http://127.0.0.1:8000/"}),
    reducerPath: "tokenApi",
    // Tag types are used for caching and invalidation.
    tagTypes: ["auth_token"],
    endpoints: (build) => ({
        // Supply generics for the return type (in this case `QuotesApiResponse`)
        // and the expected query argument. If there is no argument, use `void`
        // for the argument type instead.
        getToken: build.query<getTokenResponse, void>({
            query: () => 'token',
            // `providesTags` determines which 'tag' is attached to the
            // cached data returned by the query.
            providesTags: (result, error, id) =>
                [{type: "auth_token"}],
        }),
    }),
});

export const {useGetTokenQuery} = authApiSlice;
