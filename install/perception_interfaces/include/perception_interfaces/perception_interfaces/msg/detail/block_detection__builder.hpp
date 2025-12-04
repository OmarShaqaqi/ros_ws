// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from perception_interfaces:msg/BlockDetection.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_INTERFACES__MSG__DETAIL__BLOCK_DETECTION__BUILDER_HPP_
#define PERCEPTION_INTERFACES__MSG__DETAIL__BLOCK_DETECTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "perception_interfaces/msg/detail/block_detection__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace perception_interfaces
{

namespace msg
{

namespace builder
{

class Init_BlockDetection_confidence
{
public:
  explicit Init_BlockDetection_confidence(::perception_interfaces::msg::BlockDetection & msg)
  : msg_(msg)
  {}
  ::perception_interfaces::msg::BlockDetection confidence(::perception_interfaces::msg::BlockDetection::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return std::move(msg_);
  }

private:
  ::perception_interfaces::msg::BlockDetection msg_;
};

class Init_BlockDetection_height
{
public:
  explicit Init_BlockDetection_height(::perception_interfaces::msg::BlockDetection & msg)
  : msg_(msg)
  {}
  Init_BlockDetection_confidence height(::perception_interfaces::msg::BlockDetection::_height_type arg)
  {
    msg_.height = std::move(arg);
    return Init_BlockDetection_confidence(msg_);
  }

private:
  ::perception_interfaces::msg::BlockDetection msg_;
};

class Init_BlockDetection_width
{
public:
  explicit Init_BlockDetection_width(::perception_interfaces::msg::BlockDetection & msg)
  : msg_(msg)
  {}
  Init_BlockDetection_height width(::perception_interfaces::msg::BlockDetection::_width_type arg)
  {
    msg_.width = std::move(arg);
    return Init_BlockDetection_height(msg_);
  }

private:
  ::perception_interfaces::msg::BlockDetection msg_;
};

class Init_BlockDetection_pixel_y
{
public:
  explicit Init_BlockDetection_pixel_y(::perception_interfaces::msg::BlockDetection & msg)
  : msg_(msg)
  {}
  Init_BlockDetection_width pixel_y(::perception_interfaces::msg::BlockDetection::_pixel_y_type arg)
  {
    msg_.pixel_y = std::move(arg);
    return Init_BlockDetection_width(msg_);
  }

private:
  ::perception_interfaces::msg::BlockDetection msg_;
};

class Init_BlockDetection_pixel_x
{
public:
  explicit Init_BlockDetection_pixel_x(::perception_interfaces::msg::BlockDetection & msg)
  : msg_(msg)
  {}
  Init_BlockDetection_pixel_y pixel_x(::perception_interfaces::msg::BlockDetection::_pixel_x_type arg)
  {
    msg_.pixel_x = std::move(arg);
    return Init_BlockDetection_pixel_y(msg_);
  }

private:
  ::perception_interfaces::msg::BlockDetection msg_;
};

class Init_BlockDetection_color
{
public:
  Init_BlockDetection_color()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BlockDetection_pixel_x color(::perception_interfaces::msg::BlockDetection::_color_type arg)
  {
    msg_.color = std::move(arg);
    return Init_BlockDetection_pixel_x(msg_);
  }

private:
  ::perception_interfaces::msg::BlockDetection msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::perception_interfaces::msg::BlockDetection>()
{
  return perception_interfaces::msg::builder::Init_BlockDetection_color();
}

}  // namespace perception_interfaces

#endif  // PERCEPTION_INTERFACES__MSG__DETAIL__BLOCK_DETECTION__BUILDER_HPP_
