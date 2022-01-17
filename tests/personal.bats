load harness

@test "personal-1" {
  check '2 + 5 * 7' '37'
}

@test "personal-2" {
  check '-2 * -6' '12'
}

@test "personal-3" {
  check '5 * 30 % 7' '3'
}

@test "personal-5" {
  check '5 % 3 * 6' '12'
}

@test "personal-6" {
  check '-4 / 2 + 3 / 3 + 8' '7.0'
}

@test "personal-7" {
  check '150 + -50 / 2' '125.0'
}

@test "personal-8" {
  check '1000 / 25 * 3' '120.0'
}