<template>
  <div>
    <p>您已经被后台确认收到款的订单如下</p>
    <p>对于每个订单，您点击确认收货后将自动取消7天退货退款权</p>
    <p>对于每个订单，您点击确认收货后将自动删除</p>
    <p>对于每个订单，被后台确认收到款7天后自动收货</p>
    <p>{{mess}}</p>
    <div v-for="i in li.length" >
      <p>车辆编号{{li[i-1]['no']}}</p>
      <p>车辆类型:{{li[i-1]['name']}}</p>
      <p>车辆使用年龄:{{li[i-1]['age']}}</p>
      <p>车辆价格:{{li[i-1]['money']}}</p>
      <img  v-for="pic in li[i-1]['pics']"  :src=pic height="100px">
      <button @click="confirm(i)">确认收货</button>
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
      mess:''
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
    confirm(i){
      let no=this.li[i-1]['no']
      const form=document.querySelector("#FF");
      const formData = new FormData();
      // 向 formData 对象中添加文件
      formData.append('bike_num',no)
      console.log(formData.get('num'))
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axis.post('/confirm/', formData, config).then(res=>{
        this.mess=res.data;
        this.mess=this.mess+',车辆编号:'+no
      });
      this.li.splice(i-1,1)
    }

  }

}
</script>

<style scoped>

</style>