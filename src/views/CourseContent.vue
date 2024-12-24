<template>
    <div class="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50 p-6 md:p-12">
      <div class="max-w-4xl mx-auto">
        <div class="flex items-center justify-between mb-12">
          <h1 class="text-4xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            {{ currentCourse.name }}
          </h1>
          <div class="flex items-center gap-2 bg-white rounded-2xl px-4 py-2 shadow-md">
            <span class="text-blue-600 font-bold text-lg">{{ currentQuestionIndex + 1 }}</span>
            <span class="text-gray-400">/</span>
            <span class="text-gray-600">{{ questions.length }}</span>
          </div>
        </div>
  
        <div class="relative">
          <transition-group
            name="question-transition"
            tag="div"
            class="relative"
          >
            <div 
              v-for="(question, index) in questions"
              :key="question.id"
              v-show="currentQuestionIndex === index"
              class="transition-all duration-500"
            >
              <div class="bg-white backdrop-blur-lg rounded-[2.5rem] shadow-xl p-8 md:p-10 transform hover:shadow-2xl transition-all duration-300 border border-purple-100">
                <div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-blue-500 to-purple-600 rounded-t-[2.5rem]"></div>
                
                <div class="mb-8">
                  <span class="inline-block bg-gradient-to-r from-blue-500/10 to-purple-500/10 text-blue-700 rounded-xl px-4 py-2 text-sm font-semibold mb-4">
                    Question {{ index + 1 }}
                  </span>
                  <h3 class="text-2xl font-bold text-gray-800">{{ question.text }}</h3>
                </div>
  
                <div class="space-y-4">
                  <div
                    v-for="(option, optIndex) in question.options"
                    :key="optIndex"
                    @click="handleAnswerSelection(index, option)"
                    class="transform transition-all duration-300 hover:scale-[1.02]"
                  >
                    <div
                      class="p-6 rounded-2xl cursor-pointer transition-all duration-200 border-2"
                      :class="{
                        'bg-blue-50 border-blue-500 shadow-md': userAnswers[index] === option,
                        'border-gray-100 hover:border-blue-200 hover:bg-gray-50': userAnswers[index] !== option
                      }"
                    >
                      <div class="flex items-center gap-4">
                        <div class="w-6 h-6 rounded-full border-2 flex items-center justify-center shrink-0"
                          :class="{
                            'border-blue-500 bg-white': userAnswers[index] === option,
                            'border-gray-300': userAnswers[index] !== option
                          }"
                        >
                          <div v-if="userAnswers[index] === option" 
                            class="w-3 h-3 rounded-full bg-blue-500">
                          </div>
                        </div>
                        <span class="text-lg text-gray-700">{{ option }}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </transition-group>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        currentCourse: {},
        questions: [],
        userAnswers: {},
        currentQuestionIndex: 0,
      }
    },
    created() {
      const courseId = this.$route.params.id
      this.loadCourseData(courseId)
    },
    methods: {
      loadCourseData(courseId) {
        // Mock data - replace with actual API calls
        const courseData = {
          1: {
            name: 'Mathematics',
            questions: [
              {
                id: 1,
                text: 'What is 2 + 2?',
                options: ['3', '4', '5', '6'],
                correctAnswer: '4'
              },
              {
                id: 2,
                text: 'What is 5 × 7?',
                options: ['30', '35', '40', '45'],
                correctAnswer: '35'
              },
              {
                id: 3,
                text: 'What is 12 ÷ 3?',
                options: ['2', '3', '4', '6'],
                correctAnswer: '4'
              }
            ]
          }
        }
        
        this.currentCourse = courseData[courseId]
        this.questions = courseData[courseId].questions
      },
      handleAnswerSelection(index, answer) {
        // Save the answer
        this.userAnswers[index] = answer
        
        // Wait briefly for the answer to be visually registered
        setTimeout(() => {
          // Move to next question if available
          if (this.currentQuestionIndex < this.questions.length - 1) {
            this.currentQuestionIndex++
          } else {
            // Show completion message if it's the last question
            this.showResults()
          }
        }, 500)
      },
      showResults() {
        const totalQuestions = this.questions.length
        const correctAnswers = this.questions.reduce((count, question, index) => {
          return count + (this.userAnswers[index] === question.correctAnswer ? 1 : 0)
        }, 0)
        
        alert(`Quiz completed!\nYour score: ${correctAnswers}/${totalQuestions}`)
      }
    }
  }
  </script>
  
  <style scoped>
  .question-transition-enter-active,
  .question-transition-leave-active {
    transition: all 0.5s ease;
  }
  
  .question-transition-enter-from {
    opacity: 0;
    transform: translateY(30px);
  }
  
  .question-transition-leave-to {
    opacity: 0;
    transform: translateY(-30px);
  }
  </style>