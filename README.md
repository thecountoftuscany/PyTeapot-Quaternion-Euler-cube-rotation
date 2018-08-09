# PyTeapot-Quaternion-Euler-cube-rotation

## Introduction

Visualization of orientation of any IMU with the help of a rotating cube as per quaternions or Euler angles (strictly speaking, the [Tait Bryan Angles](https://en.wikipedia.org/wiki/Euler_angles#Tait%E2%80%93Bryan_angles)) received over the serial port using OpenGL in Python. The MPU-9250 (has on-board accelerometer, magnetometer and gyroscope) has been used with Arduino in this case:

![PyTeapot demo](https://github.com/thecountoftuscany/PyTeapot-Quaternion-Euler-cube-rotation/blob/master/resources/pyteapot-gif.gif)

This is an easy to understand Python implementation of the often-used 'MPU Teapot' processing code for the same purpose, but not specific to any particular IMU. PyGame and OpenGL are used for graphics, PySerial is used to get data from serial port.

## Usage

Most of the code is self-explanatory. However some modifications might be required as per different use cases:

- Set serial port by changing the variable `ser`.
- Set `useQuat` to `True` if receiving **quaternions** over serial and `False` if receiving **Euler angles**.
- If receiving quaternions over serial, the declination at the particular location should to be updated in `quat_to_ypr(q)` function to get correct yaw angles printed **on screen**. (The cube rotation is not dependent on this and will still work fine otherwise)

## String passed over Serial

To use this module, the data received over serial port should be in the format specified below:

- First quaternion value should be between two 'w' s
- Second quaternion value should be between two 'a' s
- Third quaternion value should be between two 'b' s
- Fourth quaternion value should be between two 'c' s
- Yaw angle should be betweem two 'y' s
- Pitch angle should be between two 'p' s
- Roll angles should be between two 'r' s

Either quaternion or Euler angles or even both can be received over the serial port. If both are received, the `useQuat` variable defines which one is used to rotate the cube. So for example, all of the following are valid formats for the data received over the serial port:

```
# Both quaternions and Euler angles
w0.09wa-0.12ab-0.09bc0.98cy168.8099yp12.7914pr-11.8401r

# Quaternions only
w0.09wa-0.12ab-0.09bc0.98c

# Euler angles only
y168.8099yp12.7914pr-11.8401r
```

Each of these must be on separate lines (or should have a '\n' at the end of the string). Other data may also be passed over Serial, provided that none of the characters w, a, b, c, y, p, r are passed (for example, `somethingw0.09wa-0.12ab-0.09bc0.98cy168.8099yp12.7914pr-11.8401rsomethingelse` is valid but `somedataw0.09wa-0.12ab-0.09bc0.98cy168.8099yp12.7914pr-11.8401ranotherstring` is not since it has the characters 'a' and 'r')

## Todo

- [ ] Receive data over WiFi instead of serial.
