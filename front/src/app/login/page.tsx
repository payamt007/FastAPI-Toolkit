"use client";

import {useForm} from "react-hook-form";

type FormValues = {
    username: string;
    password: string;
};

export default function Login() {
    const {
        register,
        handleSubmit,
        formState: {errors}
    } = useForm<FormValues>();

    const onSubmit = (data: FormValues) => {
        console.log(data); // Handle form submission (e.g., API call)
    };

    return (
        <div
            className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
            <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
                <h1 className="text-2xl font-bold">Login Page</h1>
                <p className="text-sm">Please enter your credentials to log in.</p>
                <form className="flex flex-col gap-4" onSubmit={handleSubmit(onSubmit)}>
                    <div className="flex flex-col gap-1">
                        <input
                            type="text"
                            placeholder="Username"
                            className={`border border-solid ${errors.username ? 'border-red-500' : 'border-gray-300'} rounded p-2 focus:outline-none focus:ring-2 focus:ring-blue-500`}
                            {...register("username", {
                                required: "Username is required",
                                minLength: {value: 3, message: "Username must be at least 3 characters"}
                            })}
                        />
                        {errors.username && <span className="text-red-500 text-xs">{errors.username.message}</span>}
                    </div>
                    <div className="flex flex-col gap-1">
                        <input
                            type="password"
                            placeholder="Password"
                            className={`border border-solid ${errors.password ? 'border-red-500' : 'border-gray-300'} rounded p-2 focus:outline-none focus:ring-2 focus:ring-blue-500`}
                            {...register("password", {
                                required: "Password is required",
                                minLength: {value: 6, message: "Password must be at least 6 characters"}
                            })}
                        />
                        {errors.password && <span className="text-red-500 text-xs">{errors.password.message}</span>}
                    </div>
                    <button
                        type="submit"
                        className="rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] font-medium text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 sm:w-auto"
                    >
                        Login
                    </button>
                </form>
            </main>
            <footer className="row-start-3 flex gap-[24px] flex-wrap items-center justify-center">
                <a
                    className="rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] font-medium text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 sm:w-auto"
                    href="/"
                >
                    Go to Home
                </a>
            </footer>
        </div>
    )
}