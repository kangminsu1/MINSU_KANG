#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to custom_interfaces__srv__AddTwoInts_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AddTwoInts_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub a: super::msg::Num,


    // This member is not documented.
    #[allow(missing_docs)]
    pub b: super::msg::Num,

}



impl Default for AddTwoInts_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::AddTwoInts_Request::default())
  }
}

impl rosidl_runtime_rs::Message for AddTwoInts_Request {
  type RmwMsg = super::srv::rmw::AddTwoInts_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        a: super::msg::Num::into_rmw_message(std::borrow::Cow::Owned(msg.a)).into_owned(),
        b: super::msg::Num::into_rmw_message(std::borrow::Cow::Owned(msg.b)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        a: super::msg::Num::into_rmw_message(std::borrow::Cow::Borrowed(&msg.a)).into_owned(),
        b: super::msg::Num::into_rmw_message(std::borrow::Cow::Borrowed(&msg.b)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      a: super::msg::Num::from_rmw_message(msg.a),
      b: super::msg::Num::from_rmw_message(msg.b),
    }
  }
}


// Corresponds to custom_interfaces__srv__AddTwoInts_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AddTwoInts_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub sum: super::msg::Num,

}



impl Default for AddTwoInts_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::AddTwoInts_Response::default())
  }
}

impl rosidl_runtime_rs::Message for AddTwoInts_Response {
  type RmwMsg = super::srv::rmw::AddTwoInts_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        sum: super::msg::Num::into_rmw_message(std::borrow::Cow::Owned(msg.sum)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        sum: super::msg::Num::into_rmw_message(std::borrow::Cow::Borrowed(&msg.sum)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      sum: super::msg::Num::from_rmw_message(msg.sum),
    }
  }
}






#[link(name = "custom_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__custom_interfaces__srv__AddTwoInts() -> *const std::ffi::c_void;
}

// Corresponds to custom_interfaces__srv__AddTwoInts
#[allow(missing_docs, non_camel_case_types)]
pub struct AddTwoInts;

impl rosidl_runtime_rs::Service for AddTwoInts {
    type Request = AddTwoInts_Request;
    type Response = AddTwoInts_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__custom_interfaces__srv__AddTwoInts() }
    }
}


