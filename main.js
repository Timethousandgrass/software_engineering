import Vue from 'vue/dist/vue.js';
import App from './app.vue';
// import Wel from './welcome.vue';
import VueRouter from 'vue-router';
Vue.use(VueRouter);
const routes=[
    {
        path:'/index',
        component:(resolve)=>require(['./views/welcome.vue'],resolve)
    },
    {
        path:'/signup',
        component:(resolve)=>require(['./views/sign.vue'],resolve)
    },
    {
        path:'/load',
        component:(resolve)=>require(['./views/load.vue'],resolve)
    },
    {
        path:'/upload',
        component:(resolve)=>require(['./views/upload.vue'],resolve)
    },
    {
        path:'/search',
        meta: {
            requireAuth: true,
        },
        component:(resolve)=>require(['./views/search.vue'],resolve)
    },
    {
        path:'/submit',
        component:(resolve)=>require(['./views/submit.vue'],resolve)
    },
    {
        path:'/recommand',
        component:(resolve)=>require(['./views/recommand.vue'],resolve)
    },
    {
        path:'/single/',
        name:'single',
        component:(resolve)=>require(['./views/single.vue'],resolve)
    },
    {
        path:'/buy',
        name:'buy',
        component:(resolve)=>require(['./views/buy.vue'],resolve)
    },
    {
        path:'/seller',
        component:(resolve)=>require(['./views/seller.vue'],resolve)
    },
    {
        path:'/buyer',
        component:(resolve)=>require(['./views/buyer.vue'],resolve)
    },
    {
        path:'/choose',
        component:(resolve)=>require(['./views/choose.vue'],resolve)
    },
    {
        path:'/mine',
        component:(resolve)=>require(['./views/mine.vue'],resolve)
    },
    {
        path:'/admin',
        component:(resolve)=>require(['./views/admin.vue'],resolve)
    },
    {
        path:'/confirm_paid',
        component:(resolve)=>require(['./views/confirm_paid.vue'],resolve)
    },
];


const RouterConfig={
    mode:'history',
    routes:routes
};

const router=new VueRouter(RouterConfig);
window.localStorage.setItem('loaded',false);

router.beforeEach((to,from,next)=>{
        if(to.path==='/index'){
            next();
        } else if( JSON.parse(window.localStorage.getItem('loaded'))){
            console.log('load')
            next();


        }else{
            if(to.path==='/load' || to.path==='/signup') {
                console.log('not load')
                next();
            }
        }
    }
);

new Vue({
    el:'#app',
    router:router,
    render:h=>h(App),

});




