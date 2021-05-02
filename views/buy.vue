<template>
  <div>
    <div>您需要支付{{$route.params.money}}RMB</div>
    <div>请在支付时备注您的账号以及车辆的编号，方便为您发货，请注意客服来电</div>
    <div>请注意保存您的支付记录</div>
    <div>后续客服收到款后，会根据备注的账号进行订单生成，同时会联系您进行发货</div>
    <div>您可以后续查询您的已经被后台生成的订单，订单生成可能有延迟，请您耐心等候</div>
    <img :src="'http://localhost:5555/get_file/data/OIP.jpg'" style="width: 200px;">
  </div>

</template>

<script>
export default {
  name: "buy",
}
</script>

<style scoped>

</style>