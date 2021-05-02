var path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var IP='172.18.6.189:5555'
var config = {
    entry: {
        main: './main'
    },
    output: {
        path: path.join(__dirname, './dist'),
        publicPath: '/dist/',
        filename: 'main.js'
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        css: ExtractTextPlugin.extract({
                            use: 'css-loader',
                            fallback: 'vue-style-loader'
                        })
                    }
                }
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    use: 'css-loader',
                    fallback: 'style-loader'
                })
            },
            {
                test: /\.(gif|jpg|png|woff|svg|eot|ttf)\??.*$/,
                loader: 'url-loader?limit=1024'
            },
            {
                test:/\.md$/,
                loader:'vue-markdown-loader',
                options: {
                    preprocess: function (MarkdownIt, Source) {
                        MarkdownIt.renderer.rules.table_open = function () {
                            return '<div class="table-container"><table class="table">';
                        };
                        MarkdownIt.renderer.rules.table_close = function () {
                            return '</table></div>';
                        };
                        return Source;
                    }
                }
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin("main.css")
    ],
    devServer: {
        historyApiFallback: true,
        proxy: {
            '/api':{
            // context: '/login',
            target: 'http://'+IP+'/api/',
// 代理跨域目标接口
            changeOrigin: true,
            pathRewrite:{
              '^/api':''
            }},
            '/upload':{
                // context: '/login',
                target: 'http://'+IP+'/update',
// 代理跨域目标接口
                changeOrigin: true,
                pathRewrite:{
                    '^/upload':''
            }},
            '/search':{
                // context: '/login',
                target: 'http://'+IP+'/search',
// 代理跨域目标接口
                changeOrigin: true,
                pathRewrite:{
                    '^/search':''
            }},
            '/signup':{
                target: 'http://'+IP+'/signup',
// 代理跨域目标接口
                changeOrigin: true,
                pathRewrite:{
                    '^/signup':''
            }},
            '/login':{
                target: 'http://'+IP+'/login',
// 代理跨域目标接口
                changeOrigin: true,
                pathRewrite:{
                    '^/login':''
            }},
            '/agree':{
                target: 'http://'+IP+'/agree',
// 代理跨域目标接口
                changeOrigin: true,
                pathRewrite:{
                    '^/agree':''
            }},
            '/del':{
                target: 'http://'+IP+'/del',
// 代理跨域目标接口
                changeOrigin: true,
                pathRewrite: {
                    '^/del': ''
            }},
            '/confirm':{
                target: 'http://'+IP+'/confirm',
// 代理跨域目标接口
                changeOrigin: true,
                pathRewrite: {
                    '^/confirm': ''
            }}
        }

    }
};

module.exports = config;