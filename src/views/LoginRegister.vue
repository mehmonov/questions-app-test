<template>
    <div class="min-h-screen bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center p-4">
      <div class="bg-white/90 backdrop-blur-lg p-8 rounded-3xl shadow-2xl w-full max-w-md transition-all duration-300 hover:shadow-blue-400/20">
        <div class="flex justify-center mb-8">
          <h1 class="text-3xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            Learning Platform
          </h1>
        </div>
  
        <div class="bg-gray-100 rounded-2xl p-1 mb-8">
          <div class="grid grid-cols-2 gap-1">
            <button 
              @click="isLogin = true" 
              :class="{
                'bg-white shadow-lg text-blue-600': isLogin,
                'text-gray-600 hover:bg-white/50': !isLogin
              }"
              class="py-3 rounded-xl transition-all duration-300 font-semibold"
            >
              Login
            </button>
            <button 
              @click="isLogin = false"
              :class="{
                'bg-white shadow-lg text-blue-600': !isLogin,
                'text-gray-600 hover:bg-white/50': isLogin
              }"
              class="py-3 rounded-xl transition-all duration-300 font-semibold"
            >
              Register
            </button>
          </div>
        </div>
  
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <div class="space-y-4">
            <div class="relative">
              <input
                type="email"
                v-model="email"
                placeholder="Email"
                class="w-full px-6 py-4 bg-gray-50 rounded-2xl border border-gray-200 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all duration-300 outline-none"
                required
              />
            </div>
            <div class="relative">
              <input
                type="password"
                v-model="password"
                placeholder="Password"
                class="w-full px-6 py-4 bg-gray-50 rounded-2xl border border-gray-200 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all duration-300 outline-none"
                required
              />
            </div>
          </div>
          
          <button 
            type="submit"
            class="w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white py-4 rounded-2xl hover:opacity-90 transform transition-all duration-300 hover:scale-[1.02] font-semibold text-lg shadow-lg hover:shadow-xl"
          >
            {{ isLogin ? 'Login' : 'Register' }}
          </button>
        </form>
      </div>
    </div>
  </template>

<script>
export default {
  data() {
    return {
      isLogin: true,
      email: '',
      password: ''
    }
  },
  methods: {
    handleSubmit() {
 
      this.$router.push('/courses')
    }
  }
}
</script>
