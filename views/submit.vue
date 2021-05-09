<template>
  <!--文件上传表单-->
  <form id="FF">
    <input type="text" name='name' value="fehuw" v-model="name" placeholder="请输入车辆类型">
    <input type="text" name='age' value="ifwef" v-model="age" placeholder="请输入车龄">
    <input type="text" name='money' value="ifwef" v-model="money" placeholder="请输入价格">

      <p>上传收款二维码</p>
      <input type="file"  name='上传收款二维码' value='上传收款二维码' @change="getQR($event)">



      <h>上传车辆照片</h>
      <input type="file" multiple @change="getFile($event)">

    <div v-for="i in filename">
      <p>{{i}}</p>
    </div>

    <button @click="submit($event)">提交</button>
    <p>{{mess}}</p>
  </form>

</template>

<script>
import axis from 'axios';

export default {
  // name: "submit",
  data () {
    return{
      //文件
      name:'',
      age:'',
      money:'',
      filenum:0,
      QR:[],
      file: [],
      filename:[],
      mess:''
    }
  },
  methods:{
    getFile(event) {
      let i;
      console.log(event.target)
      console.log(event.target.files)
      for(i=0;i <event.target.files.length;i++){
        this.filenum++;
        console.log(i)
        this.file.push(event.target.files[i])  ;
        this.filename.push(event.target.files[i].name)
      }
      console.log(this.filenum);
      console.log(this.file);
    },
    getQR(event){
      this.QR[0]=event.target.files[0]
    },
    submit(event) {
      event.preventDefault();//取消默认行为
      //创建 formData 对象

      const form=document.querySelector("#FF");
      const formData = new FormData();
      // 向 formData 对象中添加文件
      formData.append('account',window.localStorage.getItem('account'))
      formData.append('name',this.name)
      formData.append('age',this.age)
      formData.append('money',this.money)
      formData.append('filenum',this.filenum)
      for(let i=0; i< this.filenum;i++){
        formData.append('file'+i,this.file[i]);
      }
      formData.append('QR',this.QR[0]);

      // console.log(this.name)
      console.log(formData)
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axis.post('/upload/', formData, config).then(res=>{
        this.mess=res.data;
      });
    },
  }
}
</script>

<style scoped>

</style>