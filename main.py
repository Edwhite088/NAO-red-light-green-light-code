import cv2
import mediapipe as mp
count = 0
error = 0.005
error_check = 0.5

#draws the pose estimation
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence= 0.5, min_tracking_confidence= 0.5)
#starts video caputer
cap = cv2.VideoCapture(0)
cap.set(3, 1920 )
cap.set(4, 1080)

class move:
    def __init__(self, x, y,vis):
        self.x = x
        self.y = y
        self.vis = vis

class prev:
    def __init__(self, x, y):
        self.x = x
        self.y = y

while True:
    #capture frame by frame
    ret, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    pose_results = pose.process(img_rgb)
    mp_drawing.draw_landmarks(img, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    #uses the move class to define each part of body that we are watching
    try:
        Nose = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].visibility)
        LeftShoulder = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].visibility)
        RightShoulder = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].visibility)
        LeftElbow = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].visibility)
        RightElbow = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].visibility)
        LeftWrist = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].visibility)
        RightWrist = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].visibility)
        LeftHand = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].visibility)
        RightHand = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].visibility)
        LeftHip = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].visibility)
        RightHip = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].visibility)
        LeftKnee = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].visibility)
        RightKnee = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].visibility)
        LeftAnkle = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].visibility)
        RightAnkle = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].visibility)
        LeftFoot = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].visibility)
        RightFoot = move(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y, pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].visibility)
    except:
        print("Please put your face back in frame")

    #Makes a buffer to allow the first prev to work
    if count == 1:

        if Nose.vis > error_check:
            if Nose.x < NosePrev.x - error or Nose.x > NosePrev.x + error or Nose.y < NosePrev.y - error or Nose.y > NosePrev.y + error:
                print("Nose Moved")

        if LeftShoulder.vis > error_check:
            if LeftShoulder.x < LeftShoulderPrev.x - error or LeftShoulder.x > LeftShoulderPrev.x + error or LeftShoulder.y < LeftShoulderPrev.y - error or LeftShoulder.y > LeftShoulderPrev.y + error:
                print("Left Shoulder Moved")

        if RightShoulder.vis > error_check:
            if RightShoulder.x < RightShoulderPrev.x - error or RightShoulder.x > RightShoulderPrev.x + error or RightShoulder.y < RightShoulderPrev.y - error or RightShoulder.y > RightShoulderPrev.y + error:
                print("Right Shoulder Moved")

        if LeftElbow.vis > error_check:
            if LeftElbow.x < LeftElbowPrev.x - error or LeftElbow.x > LeftElbowPrev.x + error or LeftElbow.y < LeftElbowPrev.y - error or LeftElbow.y > LeftElbowPrev.y + error:
                print("Left Elbow Moved")

        if RightElbow.vis > error_check:
            if RightElbow.x < RightElbowPrev.x - error or RightElbow.x > RightElbowPrev.x + error or RightElbow.y < RightElbowPrev.y - error or RightElbow.y > RightElbowPrev.y + error:
                print("Right Elbow Moved")

        if LeftWrist.vis > error_check:
            if LeftWrist.x < LeftWristPrev.x - error or LeftWrist.x > LeftWristPrev.x + error or LeftWrist.y < LeftWristPrev.y - error or LeftWrist.y > LeftWristPrev.y + error:
                print("Left Wrist Moved")

        if RightWrist.vis > error_check:
            if RightWrist.x < RightWristPrev.x - error or RightWrist.x > RightWristPrev.x + error or RightWrist.y < RightWristPrev.y - error or RightWrist.y > RightWristPrev.y + error:
                print("Right Wrist Moved")

        if LeftHand.vis > error_check:
            if LeftHand.x < LeftHand.x - error or LeftHand.x > LeftHandPrev.x + error or LeftHand.y < LeftHandPrev.y - error or LeftHand.y > LeftHandPrev.y + error:
                print("Left Hand Moved")

        if RightHand.vis > error_check:
            if RightHand.x < RightHandPrev.x - error or RightHand.x > RightHandPrev.x + error or RightHand.y < RightHandPrev.y - error or RightHand.y > RightHandPrev.y + error:
                print("Right Hand Moved")

        if LeftHip.vis > error_check:
            if LeftHip.x < LeftHipPrev.x - error or LeftHip.x > LeftHipPrev.x + error or LeftHip.y < LeftHipPrev.y - error or LeftHip.y > LeftHipPrev.y + error:
                print("Left Hip Moved")

        if RightHip.vis > error_check:
            if RightHip.x < RightHipPrev.x - error or RightHip.x > RightHipPrev.x + error or RightHip.y < RightHipPrev.y - error or RightHip.y > RightHipPrev.y + error:
                print("Right Hip Moved")

        if LeftKnee.vis > error_check:
            if LeftKnee.x < LeftKneePrev.x - error or LeftKnee.x > LeftKneePrev.x + error or LeftKnee.y < LeftKneePrev.y - error or LeftKnee.y > LeftKneePrev.y + error:
                print("Left Knee Moved")

        if RightKnee.vis > error_check:
            if RightKnee.x < RightKneePrev.x - error or RightKnee.x > RightKneePrev.x + error or RightKnee.y < RightKneePrev.y - error or RightKnee.y > RightKneePrev.y + error:
                print("Right Knee Moved")

        if LeftAnkle.vis > error_check:
            if LeftAnkle.x < LeftAnklePrev.x - error or LeftAnkle.x > LeftAnklePrev.x + error or LeftAnkle.y < LeftAnklePrev.y - error or LeftAnkle.y > LeftAnklePrev.y + error:
                print("Left Ankle Moved")

        if RightAnkle.vis > error_check:
            if RightAnkle.x < RightAnklePrev.x - error or RightAnkle.x > RightAnklePrev.x + error or RightAnkle.y < RightAnklePrev.y - error or RightAnkle.y > RightAnklePrev.y + error:
                print("Right Ankle Moved")

        if LeftFoot.vis > error_check:
            if LeftFoot.x < LeftFootPrev.x - error or LeftFoot.x > LeftFootPrev.x + error or LeftFoot.y < LeftFootPrev.y - error or LeftFoot.y > LeftFootPrev.y + error:
                print("Left Foot Moved")

        if RightFoot.vis > error_check:
            if RightFoot.x < RightFootPrev.x - error or RightFoot.x > RightFootPrev.x + error or RightFoot.y < RightFootPrev.y - error or RightFoot.y > RightFootPrev.y + error:
                print("Right Foot Moved")

    try:
        NosePrev = prev(Nose.x, Nose.y)
        LeftShoulderPrev = prev(LeftShoulder.x, LeftShoulder.y)
        RightShoulderPrev = prev(RightShoulder.x, RightShoulder.y)
        LeftElbowPrev = prev(LeftElbow.x, LeftElbow.y)
        RightElbowPrev = prev(RightElbow.x, RightElbow.y)
        LeftWristPrev = prev(LeftWrist.x, LeftWrist.y)
        RightWristPrev = prev(RightWrist.x, RightWrist.y)
        LeftHandPrev = prev(LeftHand.x, LeftHand.y)
        RightHandPrev = prev(RightHand.x, RightHand.y)
        LeftHipPrev = prev(LeftHip.x, LeftHip.y)
        RightHipPrev = prev(RightHip.x, RightHip.y)
        LeftKneePrev = prev(LeftKnee.x, LeftKnee.y)
        RightKneePrev = prev(RightKnee.x, RightKnee.y)
        LeftAnklePrev = prev(LeftAnkle.x, LeftAnkle.y)
        RightAnklePrev = prev(RightAnkle.x, RightAnkle.y)
        LeftFootPrev = prev(LeftFoot.x, LeftFoot.y)
        RightFootPrev = prev(RightFoot.x, RightFoot.y)
    except:
        print("PLease Allow webcam to see you")
    count = 1
    cv2.imshow('test', img)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()