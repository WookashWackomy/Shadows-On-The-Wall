import { all, call, put, takeEvery, select } from "redux-saga/effects";
import * as api from "./api";
import {
  GET_SUBMISSIONS,
  GET_SUBMISSIONS_SUCCESS,
  SUBMISSION_UPVOTE_SUCCESS,
  SUBMISSION_UPVOTE,
  SUBMISSION_DOWNVOTE,
  SUBMISSION_DOWNVOTE_SUCCESS,
  POST_SUBMISSION,
  POST_SUBMISSION_SUCCESS
} from "./actions";
export const getSelectedTags = state => state.filtering.selectedTags;
export const getSorting = state => state.filtering.sorting;

function* postSubmission(action) {
  try {
    const { submission, submissionType } = action;
    const result = yield call(api.postSubmission, submission, submissionType);
    console.log(result);
    yield put({ type: POST_SUBMISSION_SUCCESS });
  } catch (error) {
    console.log(error);
  }
}

function* watchPostSubmission() {
  yield takeEvery(POST_SUBMISSION, postSubmission);
}

function* getSubmissions() {
  try {
    console.log("sss");
    const tags = yield select(getSelectedTags);
    const sorting = yield select(getSorting);
    const submissions = yield call(api.fetchSubmissions, tags, sorting);
    console.log(submissions);
    yield put({ type: GET_SUBMISSIONS_SUCCESS, payload: submissions });
  } catch (error) {
    console.log(error);
  }
}

function* upvoteSubmission(action) {
  try {
    console.log("upvoteSubmission");
    const response = yield call(
      api.upvoteSubmission,
      action.id,
      action.submissionType
    );
    console.log(response);
    yield put({ type: SUBMISSION_UPVOTE_SUCCESS, payload: response });
    yield put({ type: GET_SUBMISSIONS });
  } catch (error) {
    console.log(error);
  }
}

function* downvoteSubmission(action) {
  try {
    console.log("downvoteSubmission");
    const response = yield call(
      api.downvoteSubmission,
      action.id,
      action.submissionType
    );
    console.log(response);
    yield put({ type: SUBMISSION_DOWNVOTE_SUCCESS, payload: response });
    yield put({ type: GET_SUBMISSIONS });
  } catch (error) {
    console.log(error);
  }
}

function* watchUpvoteSubmission() {
  yield takeEvery(SUBMISSION_UPVOTE, upvoteSubmission);
}

function* watchDownvoteSubmission() {
  yield takeEvery(SUBMISSION_DOWNVOTE, downvoteSubmission);
}

function* watchGetSubmissions() {
  yield takeEvery(GET_SUBMISSIONS, getSubmissions);
}

export default function* submissionsSaga() {
  yield all([
    watchGetSubmissions(),
    watchUpvoteSubmission(),
    watchDownvoteSubmission(),
    watchPostSubmission()
  ]);
}
