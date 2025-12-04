// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from perception_interfaces:msg/BlockDetection.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_INTERFACES__MSG__DETAIL__BLOCK_DETECTION__STRUCT_H_
#define PERCEPTION_INTERFACES__MSG__DETAIL__BLOCK_DETECTION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'color'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/BlockDetection in the package perception_interfaces.
typedef struct perception_interfaces__msg__BlockDetection
{
  rosidl_runtime_c__String color;
  int32_t pixel_x;
  int32_t pixel_y;
  int32_t width;
  int32_t height;
  float confidence;
} perception_interfaces__msg__BlockDetection;

// Struct for a sequence of perception_interfaces__msg__BlockDetection.
typedef struct perception_interfaces__msg__BlockDetection__Sequence
{
  perception_interfaces__msg__BlockDetection * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} perception_interfaces__msg__BlockDetection__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PERCEPTION_INTERFACES__MSG__DETAIL__BLOCK_DETECTION__STRUCT_H_
