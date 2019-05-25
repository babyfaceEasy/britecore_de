<template>
  <v-container fluid>
    <v-layout row wrap>
      <v-flex xs12>
        <h1 class="text-md-center" v-text="pageTitle"></h1>
        <v-card
          class="white--text brown lighten-2 ma-2"
          v-for="risk in availableRisks"
          v-bind:key="risk.id"
        >
          <v-card-title primary-title>
            <div>
              <div class="headline">{{risk.name}}</div>
              <span>{{risk.description}}</span>
            </div>
          </v-card-title>
          <v-card-actions>
            <!--<v-btn flat dark>View Details</v-btn> -->
            <router-link :to="{ name: 'join', params: { id: risk.id }}">View Details</router-link>
          </v-card-actions>
        </v-card>

        <!-- pagination section -->
        <div class="text-xs-center">
          <v-pagination :length="0" @next="nextPage()" @previous="prevPage()"></v-pagination>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
    name: 'Menu',

    data() {
        return {
            pageTitle: 'Available Risk Types',
            availableRisks: [],
            pagination: {}
        };
    },

    created() {
        this.getAvailableRisks();
    },

    methods: {
        getAvailableRisks(api_url) {
            let vm = this;
            api_url = api_url || 'http://localhost:8000/api/v1/risk/?page=2';
            fetch(api_url)
                .then(response => response.json())
                .then(response => {
                    this.availableRisks = response.results;
                    vm.paginator(
                        response.count,
                        response.next,
                        response.previous
                    );
                })
                .catch(err => console.log(err));
        },
        paginator(count, next, prev) {
            this.pagination = {
                count,
                next,
                prev
            };
        },
        nextPage() {
            alert('kunle');
            this.getAvailableRisks(this.pagination.next);
        },
        prevPage() {
            this.getAvailableRisks(this.pagination.prev);
        },
        detailsPage() {}
    }
};
</script>

<style scoped></style>
