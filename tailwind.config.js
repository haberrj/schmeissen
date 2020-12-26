const colors = require('tailwindcss/colors')

module.exports = {
  purge: [
    './app/templates/*.html',
  ],

  darkMode: false, // or 'media' or 'class'

  theme: {
    container: {
      padding: {
        DEFAULT: '1rem',
        sm: '2rem',
        md: '3rem',
        lg: '4rem',
        xl: '5rem',
        '2xl': '6rem'
      }
    },
    fontFamily: {
      'sans': ['"Cabin"', 'sans-serif']
    },
    extend: {},
  },

  variants: {
    extend: {},
  },

  plugins: [],
}
