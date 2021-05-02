<template>
  <div>
    <input type="text" name='account' value="account" v-model="account" placeholder="请输入账号">
    <input type="text" name='bike_num' value="bike_num" v-model="bike_num" placeholder="请输入车辆编号">
    <button @click="submit($event)">提交确认信息</button>
    <p>账号:{{account}},车辆编号:{{bike_num}}   {{mess}}</p>
  </div>
</template>

<script>
import axis from "axios";
export default {
  data () {
    return{
      //文件
      account:'',
      bike_num:'',
      mess:''
    }
  },
  methods:{
    submit(event) {
      event.preventDefault();//取消默认行为
      //创建 formData 对象

      const form = document.querySelector("#FF");
      const formData = new FormData();
      // 向 formData 对象中添加文件
      formData.append('account', this.account)
      formData.append('bike_num', this.bike_num)
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axis.post('/confirm/', formData, config).then(res=>{
        this.mess=res.data;
      });
    }
  }
}
</script>

<style scoped>

</style>