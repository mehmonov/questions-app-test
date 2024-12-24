
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import LoginRegister from '../views/LoginRegister.vue'
import CourseSelection from '../views/CourseSelection.vue'
import CourseContent from '../views/CourseContent.vue'

const routes = [
  {
    path: '/',
    component: LoginRegister
  },
  {
    path: '/courses',
    component: CourseSelection
  },
  {
    path: '/course/:id',
    component: CourseContent
  }
]

export default createRouter({
  history: createWebHistory(),
  routes
})