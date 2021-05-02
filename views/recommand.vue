<template>
  <div>
    <img src="../images/grass1.jpg" style="width: 200px;">
    <p v-for="i in 2" :key="i">
      <img @click="Goto(i)" v-bind:src="'http://localhost:5555/get_file/data/'+i+'.jpg'" style="width: 200px;">
    </p>
    <img src="https://ss0.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy//it/u=2788061977,4049791815&fm=26&gp=0.jpg" style="width: 200px;">
  </div>
</template>

<script>
import axis from "axios";
export default {
  data () {
    return{
      li:[]
    }
  },
  mounted() {
    const form=document.querySelector("#FF");
    const formData = new FormData();
    // 向 formData 对象中添加文件
    formData.append('key','whatever')
    // console.log(this.name)
    console.log(formData.get('key'))
    const config = {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }
    axis.post('/search/'  ).then(res=>{
      console.log(res.data);
      this.li=res.data;
      console.log(this.li)
      console.log(this.li[0])
    });
  },
  methods:{
    Goto(i){
      this.$router.push('/single/'+i)
    }


  }
}
</script>

<style scoped>

</style>