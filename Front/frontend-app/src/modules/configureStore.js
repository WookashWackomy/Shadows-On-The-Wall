import { applyMiddleware, combineReducers, compose, createStore } from "redux";
import createSagaMiddleware from "redux-saga";
import rootSaga from "./rootSaga";
import submissionsReducer from "./Submissions/submissionsReducer";
import filteringReducer from "./Tags/filteringReducer";

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const sagaMiddleware = createSagaMiddleware();
const middleware = [sagaMiddleware];

export default () => {
  const store = createStore(
    combineReducers({
      submissions: submissionsReducer,
      filtering: filteringReducer
    }),
    composeEnhancers(applyMiddleware(...middleware))
  );

  sagaMiddleware.run(rootSaga);
  return store;
};