package com.docker;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MainController {
  @GetMapping("/")
  public String helloDocker() {
    return "Hello, Docker from Spring Boot!";
  }
}
