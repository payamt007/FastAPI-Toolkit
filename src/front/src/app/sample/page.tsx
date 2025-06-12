export default function infiniteScroll() {
    return (
        <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
        <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
            <h1 className="text-2xl font-bold">Infinite Scroll Example</h1>
            <p className="text-sm">This is a sample page demonstrating infinite scroll.</p>
        </main>
        </div>
    );
}