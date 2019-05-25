<template>
  <v-container fluid>
    <v-layout>
      <h1>Join Page</h1>
      <h5>
        <div>User {{ $route.params.id }}</div>
      </h5>
    </v-layout>
  </v-container>
</template>

<script>
export default {
    name: 'Join',
    data() {
        return {
            riskType: {}
        };
    },
    created() {
        this.getRiskTypeDetails();
    },
    methods: {
        getRiskTypeDetails(api_url, id) {
            api_url = api_url || 'http://localhost:8000/api/v1/risk/';
            api_url += this.$route.params.id;
            console.log(api_url);
            fetch(api_url)
                .then(response => response.json())
                .then(response => {
                    this.riskType = response.data;
                    console.log(this.riskType);
                })
                .catch(err => console.log(err));
        }
    }
};
</script>

<style scoped></style>
