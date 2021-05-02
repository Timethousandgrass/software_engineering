<template>
  <div>
    <p>车辆编号{{$route.params['no']}}</p>
    <p>车辆类型:{{$route.params['name']}}</p>
    <p>车辆使用年龄:{{$route.params['age']}}</p>
    <p>车辆价格:{{$route.params['money']}}</p>
    <img  v-for="pic in $route.params['pics']"  :src=pic >
    <button @click="buy($route.params['money'])">购买</button>
  </div>
</template>

<script>

export default {
  name: "single",
  data () {
    return{
      money:0,
    }
  },
  mounted() {
  },
  methods:{
    buy(money){
      this.$router.push({name:'buy',params:{money:money}})
    }


  }
}
</script>

<style scoped>

</style>