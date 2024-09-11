/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./frontend/**/*.html",
    ],
    theme: {
        extend: {
            colors: {
                'hn-orange': '#ff6600',
                'hn-background': '#f6f6ef',
                'hn-text': '#AAAAAA',
            },
        },
    },
    plugins: [],
}