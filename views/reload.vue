<template>
<<<<<<< HEAD
  <div>
    <input type="text" name='lock_code' value="" v-model="no" placeholder="请输入车辆编号">
    <button @click="submit()">重新上架</button>
    <p>{{mess}}</p>
  </div>
</template>

<script>
import axis from "axios";
export default {
name: "reload",
  data(){
    return{
      no:'',
      mess:''
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
      axis.post('/reload/', formData, config).then(res=>{
        this.mess=res.data;
      });
    }
  }
=======
$END$
</template>

<script>
export default {
name: "reload"
>>>>>>> 9d7ade600bccee4d3212d7d0f1106f99bf4a86d7
}
</script>

<style scoped>

</style>