
// src/views/CourseSelection.vue

<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50 p-6 md:p-12">
    <h1 class="text-4xl font-bold text-center mb-12 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
      Choose Your Course
    </h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-6xl mx-auto">
      <div 
        v-for="course in courses" 
        :key="course.id"
        @click="selectCourse(course)"
        class="group relative bg-white rounded-3xl shadow-xl p-8 cursor-pointer transform transition-all duration-300 hover:scale-[1.02] hover:shadow-2xl overflow-hidden"
      >
        <div class="absolute inset-0 bg-gradient-to-r from-blue-500/10 to-purple-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
        
        <div class="relative z-10">
          <div class="w-16 h-16 rounded-2xl bg-gradient-to-r from-blue-500 to-purple-600 flex items-center justify-center mb-6">
            <i :class="course.icon" class="text-white text-2xl"></i>
          </div>
          
          <h2 class="text-2xl font-bold mb-4 text-gray-800">{{ course.name }}</h2>
          <p class="text-gray-600 mb-6">{{ course.description }}</p>
          
          <div class="flex items-center text-blue-600">
            <span class="font-semibold">Start Learning</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2 group-hover:translate-x-2 transition-transform" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      courses: [
        {
          id: 1,
          name: 'Mathematics',
          description: 'Learn fundamental mathematical concepts and problem-solving skills.'
        },
        {
          id: 2,
          name: 'English',
          description: 'Improve your language skills through comprehensive exercises.'
        }
      ]
    }
  },
  methods: {
    selectCourse(course) {
      this.$router.push(`/course/${course.id}`)
    }
  }
}
</script>