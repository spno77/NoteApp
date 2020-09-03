<template>
  <div>
   <b-container>
    <h1 class="ti">My Notes </h1>
    <b-row align-v="center">
        <b-col md="3" v-for="note in notes" :key="note.id">
          <b-card 
          border-variant="info"
        header-bg-variant="info"
        header-text-variant="white" 
            :header="note.title"
            
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
           >
            <b-card-text>
              {{ note.body}}<br>
              <i>{{ note.date_created }}</i>
             
              
            </b-card-text>

          </b-card>
        </b-col>  
    </b-row>
  </b-container>
  </div>
</template>



<script>
import axios from 'axios';
 import { mapGetters } from 'vuex';

export default {
  name: 'NoteList',
  
  data(){
    return {
      notes: []
    }
  },
  computed:{
      ...mapGetters([
        'loggedUser'
      ])
     },
  mounted(){
    axios
      .get('http://127.0.0.1:8000/api/v1/notes/',
       {headers: {'Authorization': 'JWT ' + this.loggedUser.token}}  
      )
      .then(response => (this.notes = response.data))
  },

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