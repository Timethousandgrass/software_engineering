<template>
  <!--文件上传表单-->
  <form id="FF">
    <input type="text" name='name' value="fehuw" v-model="name" placeholder="请输入名字">
    <input type="text" name='age' value="ifwef" v-model="age" placeholder="请输入年龄">
    <input type="file" multiple @change="getFile($event)">
    <p v-for="i in filename">{{i}}</p>
<!--    <input type="file" @change="getFile2($event)">-->
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
      filenum:0,
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
    submit(event) {
      event.preventDefault();//取消默认行为
      //创建 formData 对象

      const form=document.querySelector("#FF");
      const formData = new FormData();
      // 向 formData 对象中添加文件
      formData.append('account',window.localStorage.getItem('account'))
      formData.append('name',this.name)
      formData.append('age',this.age)
      formData.append('filenum',this.filenum)
      for(let i=0; i< this.filenum;i++){
        formData.append('file'+i,this.file[i]);
      }

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