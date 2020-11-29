const colors = require('tailwindcss/colors')

module.exports = {
  purge: [
    './app/templates/*.html',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    colors: {
      gray: colors.coolGray,
      indigo: colors.indigo,
      green: colors.emerald,
    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
