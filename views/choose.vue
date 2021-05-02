<template>
  <div>
    <button @click="goto(0)">我是买家</button>
    <button @click="goto(1)">我是卖家</button>
    <button @click="goto(2)">我是后台管理员</button>
  </div>

</template>

<script>
export default {
  name: "choose",
  methods:{
    goto(i){
      console.log(i)
      console.log(window.localStorage.getItem('admin'))
      if (i===0){
        this.$router.push('/buyer')
      }
      else if (i===1){
        this.$router.push('/seller')
      }
      else if (i===2 && window.localStorage.getItem('admin')==='1'){
        console.log('admin')
        this.$router.push('/admin')
      }
    }
  }
}
</script>

<style scoped>


</style>