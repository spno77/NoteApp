<template>
  <div>
   <app /> 
   <b-container>
    <h1 class="ti"> Notes </h1>
    <b-row align-v="center">
        <b-col md="3" v-for="note in notes" :key="note.id">
          <b-card

            :title="note.title"
            img-src = "https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
           >
            <b-card-text>
              {{ note.body}}
            </b-card-text>

            <b-button href="#" variant="primary"> Info </b-button>
          </b-card>
        </b-col>  
    </b-row>
  </b-container>
  </div>
</template>



<script>
import axios from 'axios';
export default {
  name: 'HouseList',
  
  data(){
    return {
      notes: []
    }
  },
  mounted(){
    axios
      .get('http://127.0.0.1:8000/api/v1/notes/')
      .then(response => (this.notes = response.data))
  }
}
</script>

<style scoped>
  
.ti{
  color: lightblue;
  text-align: center;
}
.ll {
  max-width: 100%;
  max-height: 80%;
  width: auto;
  display: block;
  margin: 0 auto
}
</style> 