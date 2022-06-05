import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionDisplay from '../views/QuestionDisplay.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
import LoginDisplay from '../views/LoginDisplay.vue'
import TestReussi from '../views/TestReussi.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: '/NewQuizPage',
      name: 'NewQuizPage',
      component: NewQuizPage,
    },
    {
      path: '/questions',
      name: 'questions',
      component: QuestionDisplay,
    },
    {
      path: '/questionss',
      name: 'questionss',
      component: QuestionsManager,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginDisplay,
    },
    {
      path: '/testreussi',
      name: 'testreussi',
      component: TestReussi,
    }
  ]
})

export default router
