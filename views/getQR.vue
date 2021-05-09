<template>
  <div>
    <input type="text" name='lock_code' value="" v-model="no" placeholder="请输入车辆编号">
    <button @click="submit()">查询</button>
    <img   :src=pic height="600px">
  </div>
</template>

<script>
import axis from "axios";
export default {
  name: "getQR",
  data(){
    return{
      no:'',
      pic:''
    }
  },
  methods:{
    submit(){
      const form=document.querySelector("#FF");
      const formData = new FormData();
      // 向 formData 对象中添加文件
      formData.append('bike_num',this.no)
      // console.log(this.name)
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axis.post('/getQR/', formData, config).then(res=>{
        this.pic=res.data;
      });
    }
  }

}
</script>

<style scoped>

</style>