<template>
  <div>
    <a @click="GotoConfirm()">对收到款订单进行确认</a>
    <div v-for="i in li.length" >
      <p>车辆编号{{li[i-1]['no']}}</p>
      <p>车辆类型:{{li[i-1]['name']}}</p>
      <p>车辆使用年龄:{{li[i-1]['age']}}</p>
      <p>车辆价格:{{li[i-1]['money']}}</p>
      <img  v-for="pic in li[i-1]['pics']"  :src=pic height="100px">
      <button @click="agree(i)">同意</button>
      <button @click="del(i)">删除</button>
    </div>
  </div>
</template>

<script>
import axis from "axios";
export default {
  data () {
    return{
      li:[],
    }
  },
  mounted() {
    //创建 formData 对象
    const form=document.querySelector("#FF");
    const formData = new FormData();
    // 向 formData 对象中添加文件
    formData.append('key','admin')
    // console.log(this.name)
    console.log(formData.get('key'))
    const config = {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }
    axis.post('/search/', formData, config).then(res=>{
      console.log(res.data);
      this.li=res.data;
      console.log(this.li.length)
      console.log(this.li)
      console.log(this.li[0])
    });
  },
  methods:{
    agree(i){
      let no=this.li[i-1]['no']
      const form=document.querySelector("#FF");
      const formData = new FormData();
      // 向 formData 对象中添加文件
      formData.append('num',no)
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axis.post('/agree/', formData, config);
      this.li.splice(i-1,1)
    },
    GotoConfirm(){
      this.$router.push('/confirm_paid')
    },
    del(i){
      let no=this.li[i-1]['no']
      const form=document.querySelector("#FF");
      const formData = new FormData();
      // 向 formData 对象中添加文件
      formData.append('num',no)
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axis.post('/del/', formData, config);
      this.li.splice(i-1,1)
    }
  }
}
</script>

<style scoped>

</style>