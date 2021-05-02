<template>
  <div>
    <a @click="signup()" >注册</a>
    <a @click="login()">登录</a>
    <p>
      welcome!
    </p>
    <img src="../images/grass1.jpg" style="width: 200px;">
  </div>
</template>

<script>
export default {
  name: "welcome",
  methods:{
    signup() {
      this.$router.push('/signup')
    },
    login(){
      this.$router.push('/load')
    }
  }
}
</script>

<style scoped>

</style>