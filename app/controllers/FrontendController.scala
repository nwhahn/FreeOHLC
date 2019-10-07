package controllers

import javax.inject._
import play.api.Configuration
import play.api.http.HttpErrorHandler
import play.api.libs.json.Json
import play.api.mvc._

import scala.reflect.io.File

/**
 * Frontend controller managing all static resource associate routes.
 * @param assets Assets controller reference.
 * @param cc Controller components reference.
 */

class FrontendController @Inject()(assets: Assets, errorHandler: HttpErrorHandler, config:Configuration, cc: ControllerComponents) extends AbstractController(cc){

  //def index= assets.at("index.html")
  def index = Action {
    Ok(Json.obj("content" -> "fix to retrieve actual page"
    ))
  }

  def assetOrDefault(resource: String): Action[AnyContent] = if (resource.startsWith("/api/")){
    Action.async(r => errorHandler.onClientError(r, NOT_FOUND, "Not found"))
  } else {
    if (resource.contains(".")) assets.at(resource) else index
  }

}
