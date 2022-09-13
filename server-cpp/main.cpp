#include "crow.h"
#include <cstdio>
#include <iostream>

int main() {
  crow::SimpleApp app;

  CROW_ROUTE(app, "/").methods("POST"_method)([](const crow::request &req) {
    auto data = crow::json::load(req.body);
    if (!data) {
      return crow::response(400, "Missing request body");
    } else if (!data.has("image")) {
      return crow::response(400, "No image provided");
    } else if (!data.has("template")) {
      return crow::response(400, "No template provided");
    } else {
      auto image = std::string(data["image"]);
      auto template_image = std::string(data["template"]);
      return crow::response(200, image);
    }
  });

  app.port(18080).multithreaded().run();
}