const path = require('path');
const webpack = require('webpack');

module.exports = {
  entry: {
    index: './src/js/index.js',
    game: './src/js/game.js'
  },
  output: {
    path: path.resolve(__dirname, 'app/static/dist'),
    filename: '[name].bundle.js'
  },

  devServer: {
    contentBase: './app/static/dist'
  }
}