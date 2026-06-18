use libasciic::AsciiBuilder;
use pyo3::prelude::*;
use pyo3_stub_gen::define_stub_info_gatherer;
use std::fs::File;

use pyo3::exceptions::PyRuntimeError;
use pyo3_stub_gen::derive::gen_stub_pyfunction;

use regex::Regex;

fn trim_ascii(ascii: &str) -> String {
    let ansi_re = Regex::new(r"\x1B\[[0-9;]*m").unwrap();

    let lines: Vec<&str> = ascii.lines().collect();

    let start = lines
        .iter()
        .position(|line| !ansi_re.replace_all(line, "").trim().is_empty())
        .unwrap_or(0);

    let end = lines
        .iter()
        .rposition(|line| !ansi_re.replace_all(line, "").trim().is_empty())
        .map(|i| i + 1)
        .unwrap_or(lines.len());

    lines[start..end].join("\n")
}

#[gen_stub_pyfunction]
#[pyfunction]
fn image_to_ascii(path_image: String, width: u32, height: u32) -> PyResult<String> {
    let file = File::open(path_image)?;

    let ascii = AsciiBuilder::new(file)
        .dimensions(width, height)
        .colorize(true)
        .make_ascii()
        .map_err(|e| PyRuntimeError::new_err(e.to_string()))?;

    let ascii = trim_ascii(&ascii);

    Ok(ascii)
}

#[pymodule]
fn choco_coco_image_to_ascii(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(image_to_ascii, m)?)?;

    Ok(())
}

define_stub_info_gatherer!(stub_info);
