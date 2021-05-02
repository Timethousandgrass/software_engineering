<template>
  <div>
    <div>
      <!-- 使用 router-link 组件来导航. -->
      <!-- 通过传入 `to` 属性指定链接. -->
      <!-- <router-link> 默认会被渲染成一个 `<a>` 标签 -->

      <!--      <router-link to="/signup">go to signup</router-link>-->
      <!--      <router-link to="/load">go to load</router-link>-->
      <!--      <router-link to="/upload">Go to upload</router-link>-->
      <router-link to="/search">Go to search</router-link>
      <router-link to="/mine">Go to mine</router-link>
      <!--      <router-link to="/submit">Go to submit</router-link>-->
      <!--      <router-link to="/recommand">Go to recommand</router-link>-->
    </div>

    <router-view></router-view>

  </div>
</template>

<script>
export default {
  name: "buyer",
  mounted() {
    this.$router.push('/search')
  },
  components:{
  }
}
</script>

<style scoped>

</style>