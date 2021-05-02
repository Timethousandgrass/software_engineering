<template>
  <div>
    <!--文件上传表单-->
    <form id="FF">
      <input type="text" name='Account' value="20180000" v-model="account" placeholder="请输入学号">
      <input type="text" name='password' value="" v-model="password" placeholder="请输入密码">
      <input type="text" name='phone_num' value="" v-model="phone_num" placeholder="请输入联系方式">
      <button @click="submit($event)">注册</button>
    </form>
    <p>
      {{mess}}
    </p>
  </div>
</template>

<script>
import axis from 'axios';

export default {
  data () {
    return{
      //文件
      account:'',
      password:'',
      mess:'',
      phone_num:''

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
      formData.append('password', this.password)
      formData.append('phone_num', this.phone_num)
      console.log(formData.get('account'))
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axis.post('/signup/', formData, config).then(res=>{
        console.log("res: ", res);
        this.mess=res.data
        if (this.mess==="True") {
          console.log('here');
          this.$router.push('/load')
        }else{
          console.log('biao')
        }
      });
    }
  }
}
</script>

<style scoped>

</style>