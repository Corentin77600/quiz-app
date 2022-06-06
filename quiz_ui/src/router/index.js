import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionDisplay from '../views/QuestionDisplay.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
import LoginDisplay from '../views/LoginDisplay.vue'
import AdministrationDisplay from '../views/AdministrationDisplay.vue'

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
      path: '/questionss',
      name: 'questionss',
      component: QuestionDisplay,
    },
    {
      path: '/questions',
      name: 'questions',
      component: QuestionsManager,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginDisplay,
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdministrationDisplay,
    }
  ]
})

export default router
