use libasciic::{AsciiBuilder, Style};
use pyo3::prelude::*;
use pyo3_stub_gen::define_stub_info_gatherer;
use std::fs::File;

use pyo3::exceptions::PyRuntimeError;
use pyo3_stub_gen::derive::gen_stub_pyfunction;

#[gen_stub_pyfunction]
#[pyfunction]
fn image_to_ascii(path_image: String, width: u32, height: u32) -> PyResult<String> {
    let file = File::open(path_image)?;

    let ascii = AsciiBuilder::new(file)
        .dimensions(width, height)
        .colorize(true)
        .style(Style::FgPaint)
        .make_ascii()
        .map_err(|e| PyRuntimeError::new_err(e.to_string()))?;

    Ok(ascii)
}

#[pymodule]
fn choco_coco_image_to_ascii(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(image_to_ascii, m)?)?;

    Ok(())
}

define_stub_info_gatherer!(stub_info);
