import eyetracking as eye

ets = eye.EyeTrackingStudy("dataset")
ets.load_data()
print(ets.gazes.sample(10))
