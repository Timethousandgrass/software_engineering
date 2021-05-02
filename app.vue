<template>
  <div>
    <div>
      <!-- 使用 router-link 组件来导航. -->
      <!-- 通过传入 `to` 属性指定链接. -->
      <!-- <router-link> 默认会被渲染成一个 `<a>` 标签 -->

<!--      <router-link to="/signup">go to signup</router-link>-->
<!--      <router-link to="">go to load</router-link>-->
<!--      <router-link to="/upload">Go to upload</router-link>-->
<!--      <router-link to="/search">Go to search</router-link>-->
<!--      <router-link to="/submit">Go to submit</router-link>-->
<!--      <router-link to="/recommand">Go to recommand</router-link>-->
    </div>

    <router-view></router-view>
  </div>
</template>
<script>
import vTitle from './title.vue';
import vButton from './button.vue';



// import markdown from './a.md'
// import VueMarkdown from 'vue-markdown'

export default {
  mounted() {
    this.$router.push('/index')
  },
  data: function () {
    return {}
  },
  components: {
    vTitle,
    vButton,
  },
  methods: {

  }
}
</script>