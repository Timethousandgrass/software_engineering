<template>
  <div>
    <p>您已经被后台确认的订单如下</p>
    <div v-for="item in li">
      <p>车辆编号{{item['no']}}</p>
      <p>车辆类型:{{item['name']}}</p>
      <p>车辆使用年龄:{{item['age']}}</p>
      <p>车辆价格:{{item['money']}}</p>
      <img  v-for="pic in item['pics']"  :src=pic>
    </div>
  </div>

</template>

<script>
import axis from "axios";
export default {
  name: "mine",
  data(){
    return{
      li:[],
    }
  },
  mounted() {
    console.log('overhere')

    const form=document.querySelector("#FF");
    const formData = new FormData();
    // 向 formData 对象中添加文件
    formData.append('key',window.localStorage.getItem('account'))
    const config = {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }
    axis.post('/search/', formData, config).then(res=>{
      console.log(res.data);
      this.li=res.data;
      console.log(this.li)
      console.log(this.li[0])
    });
  },
  methods:{

  }

}
</script>

<style scoped>

</style>